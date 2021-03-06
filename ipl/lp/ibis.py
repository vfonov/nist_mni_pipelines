import os
# for xml manipulation
from string import Template

def save_ibis_summary(iter_summary,
                 fname):
    """
    Save a scene containing the volumes calculated by the pipeline.
    The volumes are the registered head image, the brain mask, the cortex
    surface, and the skin surface. The scene is stored in fname.

    Arguments: iter_summary Dictionary containing all the filenames
               fname Path of the output scene file
    """

    #Set xml structure

    default_xml = Template("""<!DOCTYPE configML>
    <configuration>
     <SaveScene>
      <IbisVersion value="3.0.0  Dev"/>
      <IbisRevision value="4a50db1"/>
      <Version value="6.0"/>
      <NextObjectID value="5"/>
      <NumberOfSceneObjects value="7"/>
      <ObjectList>
       <ObjectInScene_0>
        <ObjectClass value="WorldObject"/>
        <FullFileName value="none"/>
        <ObjectID value="-2"/>
        <ParentID value="-1"/>
        <ObjectName value="World"/>
        <AllowChildren value="1"/>
        <AllowChangeParent value="0"/>
        <ObjectManagedBySystem value="1"/>
        <ObjectHidden value="0"/>
        <AllowHiding value="0"/>
        <ObjectDeletable value="0"/>
        <NameChangeable value="0"/>
        <ObjectListable value="1"/>
        <AllowManualTransformEdit value="0"/>
        <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
       </ObjectInScene_0>
       <ObjectInScene_1>
        <ObjectClass value="TripleCutPlaneObject"/>
        <FullFileName value="none"/>
        <ObjectID value="-3"/>
        <ParentID value="-2"/>
        <ViewPlanes value="1 1 1 "/>
        <PlanesPosition value="-9.0635992929070994e+00 -2.8457999184123580e+01 2.7191258146407492e+01 "/>
        <SliceThickness value="1"/>
        <SliceMixMode>
         <NumberOfElements value="2"/>
         <Element_0 value="2"/>
         <Element_1 value="2"/>
        </SliceMixMode>
        <BlendingModeIndices>
         <NumberOfElements value="2"/>
         <Element_0 value="2"/>
         <Element_1 value="2"/>
        </BlendingModeIndices>
       </ObjectInScene_1>
       <ObjectInScene_2>
        <ObjectClass value="VolumeRenderingObject"/>
        <FullFileName value="none"/>
        <ObjectID value="-5"/>
        <ParentID value="-2"/>
        <ObjectName value="PRISM Volume Render"/>
        <AllowChildren value="0"/>
        <AllowChangeParent value="0"/>
        <ObjectManagedBySystem value="1"/>
        <ObjectHidden value="1"/>
        <AllowHiding value="1"/>
        <ObjectDeletable value="0"/>
        <NameChangeable value="0"/>
        <ObjectListable value="1"/>
        <AllowManualTransformEdit value="0"/>
        <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
        <IsAnimating value="0"/>
        <SamplingDistance value="1.0000000000000000e+00"/>
        <ShowInteractionWidget value="0"/>
        <InteractionWidgetLine value="0"/>
        <InteractionPoint1 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 "/>
        <InteractionPoint2 value="2.0000000000000000e+02 0.0000000000000000e+00 0.0000000000000000e+00 "/>
        <RayInitShaderTypeName value="None"/>
        <StopConditionShaderTypeName value="ERT alpha 99%"/>
        <ImageSlots>
         <NumberOfElements value="1"/>
         <Element_0>
          <VolumeEnabled value="1"/>
          <VolumeIs16Bits value="0"/>
          <LinearSampling value="1"/>
          <ShaderContributionTypeName value="Add"/>
          <LastImageObjectId value="0"/>
          <ColorTransferFunction>
           <NbColorPoints value="2"/>
           <ColorPoint_0 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
           <ColorPoint_1 value="2.5500000000000000e+02 1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
          </ColorTransferFunction>
          <OpacityTransferFunction>
           <NbPoints value="2"/>
           <Point_0 value="1.1316568047337279e+00 4.0000000000000001e-02 5.0000000000000000e-01 0.0000000000000000e+00 "/>
           <Point_1 value="2.5349112426035504e+02 9.7599999999999998e-01 5.0000000000000000e-01 0.0000000000000000e+00 "/>
          </OpacityTransferFunction>
         </Element_0>
        </ImageSlots>
       </ObjectInScene_2>
       <ObjectInScene_3>
        <ObjectClass value="ImageObject"/>
        <FullFileName value="./$replace_main_image_path"/>
        <ObjectID value="0"/>
        <ParentID value="-2"/>
        <ObjectName value="$replace_main_image_name"/>
        <AllowChildren value="1"/>
        <AllowChangeParent value="1"/>
        <ObjectManagedBySystem value="0"/>
        <ObjectHidden value="0"/>
        <AllowHiding value="1"/>
        <ObjectDeletable value="1"/>
        <NameChangeable value="1"/>
        <ObjectListable value="1"/>
        <AllowManualTransformEdit value="1"/>
        <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
        <LabelImage value="0"/>
        <ViewOutline value="0"/>
        <LutIndex value="0"/>
        <LutRange value="-9.3311071395874023e+00 3.1488708496093750e+02 "/>
        <IntensityFactor value="9.8999999999999999e-01"/>
        <VolumeRenderingEnabled value="0"/>
        <ColorWindow value="1.0000000000000000e+00"/>
        <ColorLevel value="5.0000000000000000e-01"/>
        <EnableShading value="0"/>
        <Ambiant value="1.0000000000000001e-01"/>
        <Diffuse value="6.9999999999999996e-01"/>
        <Specular value="2.0000000000000001e-01"/>
        <SpecularPower value="1.0000000000000000e+01"/>
        <EnableGradientOpacity value="1"/>
        <AutoSampleDistance value="1"/>
        <SampleDistance value="1.0000000000000000e+00"/>
        <ShowVolumeClippingBox value="0"/>
        <VolumeRenderingBounds value="-9.6000000000000000e+01 9.6000000000000000e+01 -1.3200000000000000e+02 9.6000000000000000e+01 -7.8000000000000000e+01 1.1400000000000000e+02 "/>
        <ScalarOpacity>
         <NbPoints value="2"/>
         <Point_0 value="0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
         <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
        </ScalarOpacity>
        <GradientOpacity>
         <NbPoints value="2"/>
         <Point_0 value="0.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
         <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
        </GradientOpacity>
        <ColorTransferFunction>
         <NbColorPoints value="2"/>
         <ColorPoint_0 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
         <ColorPoint_1 value="2.5500000000000000e+02 1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
        </ColorTransferFunction>
       </ObjectInScene_3>
       <ObjectInScene_4>
        <ObjectClass value="ImageObject"/>
        <FullFileName value="./$replace_mask_path"/>
        <ObjectID value="1"/>
        <ParentID value="-2"/>
        <ObjectName value="$replace_mask_name"/>
        <AllowChildren value="1"/>
        <AllowChangeParent value="1"/>
        <ObjectManagedBySystem value="0"/>
        <ObjectHidden value="0"/>
        <AllowHiding value="1"/>
        <ObjectDeletable value="1"/>
        <NameChangeable value="1"/>
        <ObjectListable value="1"/>
        <AllowManualTransformEdit value="1"/>
        <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
        <LabelImage value="0"/>
        <ViewOutline value="0"/>
        <LutIndex value="0"/>
        <LutRange value="-9.2964763641357422e+00 1.7405364990234375e+02 "/>
        <IntensityFactor value="9.8999999999999999e-01"/>
        <VolumeRenderingEnabled value="0"/>
        <ColorWindow value="1.0000000000000000e+00"/>
        <ColorLevel value="5.0000000000000000e-01"/>
        <EnableShading value="0"/>
        <Ambiant value="1.0000000000000001e-01"/>
        <Diffuse value="6.9999999999999996e-01"/>
        <Specular value="2.0000000000000001e-01"/>
        <SpecularPower value="1.0000000000000000e+01"/>
        <EnableGradientOpacity value="1"/>
        <AutoSampleDistance value="1"/>
        <SampleDistance value="1.0000000000000000e+00"/>
        <ShowVolumeClippingBox value="0"/>
        <VolumeRenderingBounds value="-9.6000000000000000e+01 9.6000000000000000e+01 -1.3200000000000000e+02 9.6000000000000000e+01 -7.8000000000000000e+01 1.1400000000000000e+02 "/>
        <ScalarOpacity>
         <NbPoints value="2"/>
         <Point_0 value="0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
         <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
        </ScalarOpacity>
        <GradientOpacity>
         <NbPoints value="2"/>
         <Point_0 value="0.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
         <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
        </GradientOpacity>
        <ColorTransferFunction>
         <NbColorPoints value="2"/>
         <ColorPoint_0 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
         <ColorPoint_1 value="2.5500000000000000e+02 1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
        </ColorTransferFunction>
       </ObjectInScene_4>
       <ObjectInScene_5>
        <ObjectClass value="PolyDataObject"/>
        <FullFileName value="./$replace_cortex_surface_path"/>
        <ObjectID value="2"/>
        <ParentID value="-2"/>
        <ObjectName value="$replace_cortex_surface_name"/>
        <AllowChildren value="1"/>
        <AllowChangeParent value="1"/>
        <ObjectManagedBySystem value="0"/>
        <ObjectHidden value="0"/>
        <AllowHiding value="1"/>
        <ObjectDeletable value="1"/>
        <NameChangeable value="1"/>
        <ObjectListable value="1"/>
        <AllowManualTransformEdit value="1"/>
        <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
        <RenderingMode value="2"/>
        <LutIndex value="0"/>
        <ScalarsVisible value="0"/>
        <VertexColorMode value="0"/>
        <ScalarSourceObjectId value="-1"/>
        <Opacity value="1.0000000000000000e+00"/>
        <ObjectColor value="1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 "/>
        <CrossSectionVisible value="0"/>
        <ClippingEnabled value="0"/>
        <ClippingPlanesOrientation value="1 1 1 "/>
        <ShowTexture value="0"/>
        <TextureFileName value=""/>
       </ObjectInScene_5>
       <ObjectInScene_6>
        <ObjectClass value="PolyDataObject"/>
        <FullFileName value="./$replace_skin_surface_path"/>
        <ObjectID value="4"/>
        <ParentID value="-2"/>
        <ObjectName value="$replace_skin_surface_name"/>
        <AllowChildren value="1"/>
        <AllowChangeParent value="1"/>
        <ObjectManagedBySystem value="0"/>
        <ObjectHidden value="1"/>
        <AllowHiding value="1"/>
        <ObjectDeletable value="1"/>
        <NameChangeable value="1"/>
        <ObjectListable value="1"/>
        <AllowManualTransformEdit value="1"/>
        <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
        <RenderingMode value="2"/>
        <LutIndex value="0"/>
        <ScalarsVisible value="0"/>
        <VertexColorMode value="0"/>
        <ScalarSourceObjectId value="-1"/>
        <Opacity value="1.0000000000000000e+00"/>
        <ObjectColor value="1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 "/>
        <CrossSectionVisible value="0"/>
        <ClippingEnabled value="0"/>
        <ClippingPlanesOrientation value="1 1 1 "/>
        <ShowTexture value="0"/>
        <TextureFileName value=""/>
       </ObjectInScene_6>
      </ObjectList>
      <Plugins>
       <USAcquisitionDoubleView/>
       <SEEGAtlas/>
      </Plugins>
      <SceneManager>
       <CurrentObjectID value="4"/>
       <ReferenceObjectID value="0"/>
       <ViewBackgroundColor value="0.0000000000000000e+00 0.0000000000000000e+00 4.9803921568627452e-01 "/>
       <View3DBackgroundColor value="0.0000000000000000e+00 0.0000000000000000e+00 4.9803921568627452e-01 "/>
       <Views>
        <NumberOfViews value="4"/>
        <View_0>
         <ViewID value="-2"/>
         <ViewType value="2"/>
         <Name value="Transverse"/>
         <Position value="0.0000000000000000e+00 -1.8000000000000000e+01 5.9383439472723376e+02 "/>
         <FocalPoint value="0.0000000000000000e+00 -1.8000000000000000e+01 1.8000000000000000e+01 "/>
         <Scale value="6.3166315072106393e+01"/>
         <ViewUp value="0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 "/>
         <ViewAngle value="3.0000000000000000e+01"/>
        </View_0>
        <View_1>
         <ViewID value="-3"/>
         <ViewType value="3"/>
         <Name value="ThreeD"/>
         <Position value="5.2109475696103266e+02 -1.2685995307647572e+02 4.8483440068776019e+01 "/>
         <FocalPoint value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 "/>
         <Scale value="2.5980762113533160e+02"/>
         <ViewUp value="0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
         <ViewAngle value="3.0000000000000000e+01"/>
        </View_1>
        <View_2>
         <ViewID value="-4"/>
         <ViewType value="1"/>
         <Name value="Coronal"/>
         <Position value="0.0000000000000000e+00 -5.4255375505322445e+02 1.8000000000000000e+01 "/>
         <FocalPoint value="0.0000000000000000e+00 -1.8000000000000000e+01 1.8000000000000000e+01 "/>
         <Scale value="6.5009256279320482e+01"/>
         <ViewUp value="0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
         <ViewAngle value="3.0000000000000000e+01"/>
        </View_2>
        <View_3>
         <ViewID value="-5"/>
         <ViewType value="0"/>
         <Name value="Sagittal"/>
         <Position value="-5.7583439472723376e+02 -1.8000000000000000e+01 1.8000000000000000e+01 "/>
         <FocalPoint value="0.0000000000000000e+00 -1.8000000000000000e+01 1.8000000000000000e+01 "/>
         <Scale value="9.5406885948819266e+01"/>
         <ViewUp value="0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
         <ViewAngle value="3.0000000000000000e+01"/>
        </View_3>
       </Views>
      </SceneManager>
      <AxesHidden value="0"/>
      <CursorVisible value="1"/>
      <CutPlanesCursorColor_r value="50"/>
      <CutPlanesCursorColor_g value="50"/>
      <CutPlanesCursorColor_b value="50"/>
      <QuadViewWindow>
       <CurrentViewWindow value="1"/>
       <ViewExpanded value="0"/>
      </QuadViewWindow>
      <Plugins>
       <GeneratedSurface/>
       <LabelVolumeToSurfaces/>
       <LandmarkRegistrationObject/>
       <PRISMVolumeRender/>
       <USAcquisitionDoubleView/>
       <SEEGAtlas/>
      </Plugins>
     </SaveScene>
    </configuration>
    """)

    #Replace correspoding image names in the xml scene

    xml_modified = default_xml.substitute(
                        replace_main_image_path = os.path.relpath(iter_summary['t1w_tal_noscale'].scan, iter_summary['output_dir']),
                        replace_main_image_name = iter_summary['t1w_tal_noscale'].name,
                        replace_mask_path = os.path.relpath(iter_summary['t1w_tal_noscale_mask'].scan, iter_summary['output_dir']),
                        replace_mask_name = iter_summary['t1w_tal_noscale_mask'].name,
                        replace_cortex_surface_path = os.path.relpath(iter_summary['cortex_surface'].fname, iter_summary['output_dir']),
                        replace_cortex_surface_name = iter_summary['cortex_surface'].name,
                        replace_skin_surface_path = os.path.relpath(iter_summary['skin_surface'].fname, iter_summary['output_dir']),
                        replace_skin_surface_name = iter_summary['skin_surface'].name
                        )

    file_out = open(fname, "wt")
    file_out.write(xml_modified)
    file_out.close()
